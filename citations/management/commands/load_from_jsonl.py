import json
import os
import subprocess

from django.core.management.base import BaseCommand
from django.db.utils import DataError

from citations.models import Citation


class Command(BaseCommand):
    help = '''Importa os dados de citações de um arquivo JSONL.'''

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.field_mapping = [
            ('cited_issnl', 'issn'), 
            ('cited_journal', 'title'), 
            ('cited_vol', 'volume'), 
            ('cited_year', 'year'),
            ('citing_pid', 'citation_code'),
            ('issnls_size', 'issn_size_set'),
            ('result_code', 'standardization_method'),
            ('title_year_volume_key', 'standardization_key'),
        ]

    def add_arguments(self, parser):
        parser.add_argument(
            '--citations',
            default='citations.jsonl',
            help='Nome do arquivo de citações',
            type=str,
        )

    def _standardize_citation_code(self, citation):
        els = citation.citation_code.split('^c')
        citation.citation_code = '-'.join(els)

    def handle(self, *args, **options):
        filename = options.get('citations')

        if not os.path.exists(filename):
            self.stdout.write(self.style.ERROR(f'Arquivo de citações não encontrado: {filename}'))
            return

        try:
            self.run_import(filename, self.field_mapping)
        except subprocess.CalledProcessError as e:
            self.stdout.write(self.style.ERROR(f'Erro ao executar comando: {e.cmd}'))

    def run_import(self, file, field_mapping):
        self.stdout.write('Importando dados do JSONL para o PostgreSQL')
        self.stdout.write(f'Origem: {file}')

        with open(file) as fin:
            counter = 0

            for row in fin:
                json_row = json.loads(row)

                counter += 1
                if counter % 1000 == 0:
                    self.stdout.write(f'{counter} linhas processadas')
                
                cit = Citation()
                for f in field_mapping:
                    source, target = f
                    value = json_row.get(source)
                    if value:
                        setattr(cit, target, value)

                self._standardize_citation_code(cit)
                   
                try:
                    cit.save()
                except DataError:
                    self.stdout.write(f'Não foi possível gravar registro {row}')

{
   'name': 'Airproof Theme',
   'description': '...',
   'category': 'Theme/Corporate',
   'sequence': 110,
   'version': '2.0.0',
   'author': 'Odoo S.A.',
   'data': [
      'data/ir_asset.xml',
      'views/website_templates.xml',
   ],
   'assets': {
      'web._assets_primary_variables': [
         ('append', 'website_airproof/static/src/scss/primary_variables.scss'),
      ],
      # 'web.assets_frontend': [
      #    'website_airproof/static/src/scss/font.scss',
      #    'website_airproof/static/src/scss/theme.scss',
      #    'website_airproof/static/src/js/theme.js',
      # ],
      # 'web._assets_frontend_helpers': [
      #    ('prepend', 'website_airproof/static/src/scss/bootstrap_overridden.scss'),
      # ],
   },
   'snippet_lists': {
      'homepage': ['external_snippets'],
   },
   'depends': ['theme_common', 'website'],
   'license': 'LGPL-3',
}

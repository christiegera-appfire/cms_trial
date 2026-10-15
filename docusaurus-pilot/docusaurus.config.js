// @ts-check
// Pilot config. noIndex keeps this out of Google while it is a test site.
// BASE_URL: '/' for a custom domain, '/repo-name/' for GitHub project Pages.
const baseUrl = process.env.BASE_URL || '/';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Appfire Docs (pilot)',
  tagline: 'Docs-as-code pilot',
  url: process.env.SITE_URL || 'http://localhost:3000',
  baseUrl,
  noIndex: true,
  onBrokenLinks: 'warn', // broken links print as warnings so we can read them, not fail the build
  markdown: { format: 'detect' },
  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/', // docs at the site root so slugs match the current URL scheme
          sidebarPath: './sidebars.js',
          showLastUpdateTime: true,
          editUrl: 'https://appfire.atlassian.net/wiki', // each page overrides with custom_edit_url
        },
        blog: false,
        theme: { customCss: './src/css/custom.css' },
      },
    ],
  ],
  themeConfig: {
    colorMode: { defaultMode: 'dark', respectPrefersColorScheme: false },
    navbar: { title: 'Appfire Docs' },
    docs: { sidebar: { hideable: true } },
  },
};

module.exports = config;

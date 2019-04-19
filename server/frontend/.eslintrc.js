module.exports = {
  root: true,
  env: {
    node: true,
    browser: true,
    jquery: true,
  },
  extends: [
    'plugin:vue/essential',
    '@vue/airbnb',
  ],
  rules: {
    'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-unused-import': 'off',
    'no-tabs': 'off',
    'max-len': 'off',
    'no-plusplus': 'off',
    indent: 'off',
    'no-unused-expressions': ['error', { allowTernary: true }],
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
};

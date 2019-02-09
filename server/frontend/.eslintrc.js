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
    'no-unused-import' : 'off',
    'no-tabs' : 'off',
    'max-len' : 'off'
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
};

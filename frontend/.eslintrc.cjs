module.exports = {
  root: true,
  env: {
    browser: true,
    node: true
  },
  extends: [
    '@nuxt/eslint'
  ],
  rules: {
    'vue/multi-word-component-names': 'off'
  }
}


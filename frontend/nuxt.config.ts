// https://nuxt.com/docs/api/configuration/nuxt-config
import tailwindcss from "@tailwindcss/vite"

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  css: ['~/assets/css/main.css'],
  modules: [
    '@nuxt/eslint',
    '@nuxt/fonts',
    '@nuxt/icon',
    '@nuxt/image',
    '@nuxt/scripts',
    '@nuxt/ui'
  ],
  vite: {
    plugins: [
      tailwindcss(),
    ],
  },
  devServer: {
    host: '127.0.0.1'
  },
  runtimeConfig: {
    public: {
      baseUrl: ''
    }
  }
})
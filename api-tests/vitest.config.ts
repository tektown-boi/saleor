import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    include: [__dirname + '*/tests/**/*.test.ts'],
    env: {
      apiEndpoint: 'https://master.staging.saleor.cloud/graphql/',
    },
  },
})

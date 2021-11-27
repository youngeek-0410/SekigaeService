import { Layout } from 'page/layouts/Layout'
import type { AppProps } from 'next/app'

import { ChakraProvider } from '@chakra-ui/react'
import theme from 'assets/theme'

function App({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider theme={theme}>
      <Layout>
        < Component {...pageProps} />
      </Layout>
    </ChakraProvider>
  )
}

export default App

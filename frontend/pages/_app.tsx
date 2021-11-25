import { Layout } from 'page/layouts/Layout'
import { ChakraProvider } from '@chakra-ui/react'
import type { AppProps } from 'next/app'

function App({ Component, pageProps }: AppProps) {
  return (
    <ChakraProvider>
      <Layout>
        < Component {...pageProps} />
      </Layout>
    </ChakraProvider>
  )
}

export default App

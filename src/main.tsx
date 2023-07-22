import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import { ChakraProvider } from '@chakra-ui/react'
import {QueryClient, QueryClientProvider} from 'react-query'
import './index.css'

import { extendTheme } from '@chakra-ui/react'

const theme = extendTheme({
  fonts: {
    heading: `'Poppins', sans-serif`,
    body: `'Poppins', sans-serif`,
  },
})

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <QueryClientProvider client={new QueryClient()}>
        <ChakraProvider theme={theme}>
          <App />
        </ChakraProvider>
    </QueryClientProvider>
  </React.StrictMode>,
)

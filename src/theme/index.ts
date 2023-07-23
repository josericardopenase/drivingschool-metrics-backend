import { extendTheme } from '@chakra-ui/react'
import foundations from './foundations'

const direction = 'ltr'

const config = {
  useSystemColorMode: false,
  initialColorMode: 'light',
  cssVarPrefix: 'chakra',
}

export const theme = {
  direction,
  ...foundations,
  config,
  fonts: {
    heading: `'Poppins', sans-serif`,
    body: `'Poppins', sans-serif`,
  },
}

export default extendTheme(theme)

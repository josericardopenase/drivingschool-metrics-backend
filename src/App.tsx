import './App.css'
import { RouterProvider } from 'react-router-dom'
import router from './routes/router'
import '@fontsource/poppins/400.css'
import '@fontsource/poppins/500.css'
import '@fontsource/poppins/600.css'
import '@fontsource/poppins/700.css'
import '@fontsource/poppins/800.css'
import '@fontsource/poppins/900.css'

function App() {
  return (
    <RouterProvider router={router} />
  )
}

export default App

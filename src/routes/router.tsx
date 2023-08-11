import { createBrowserRouter } from "react-router-dom";
import Login from "../pages/auth/Login";
import Dashboard from "../pages/app/Dashboard";
import NotAuthOnly from "../components/guards/NotAuthOnly";
import AuthOnly from "../components/guards/AuthOnly";
import App from "../App";
import AppContainer from "../pages/app";
import Permissions from "../pages/app/Permissions";
import Sections from "../pages/app/Sections";

const router = createBrowserRouter([
    {
      path: "/login",
      element: <NotAuthOnly></NotAuthOnly>,
      children: [
        {
          index: true,
          element: <Login/>
        }
      ]
    },
    {
      path: '/',
      element: <AuthOnly></AuthOnly>,
      children: [
        {
          path: '',
          element: <AppContainer></AppContainer>,
          children : [
            {
              index: true,
              element: <Dashboard></Dashboard>,
            },
            {
              path: "/permissions",
              element: <Permissions></Permissions>,
            },
            {
              path: "/sections",
              element: <Sections></Sections>
            }
          ]
        }
        
      ]
    }
  ]);

export default router
import { createBrowserRouter } from "react-router-dom";
import Login from "../pages/auth/Login";
import Dashboard from "../pages/app/Dashboard";
import NotAuthOnly from "../components/guards/NotAuthOnly";
import AuthOnly from "../components/guards/AuthOnly";

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
          index: true,
          element: <Dashboard/>
        }
      ]
    }
  ]);

export default router
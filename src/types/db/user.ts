export  interface User {
    id: number;
    last_login: string;
    is_superuser: boolean;
    username: string;
    first_name: string;
    last_name: string;
    email: string;
    is_staff: boolean;
    is_active: boolean;
    date_joined: string;
    groups: any[]; // If you have a specific type for groups, replace `any[]` with that type
    user_permissions: any[]; // If you have a specific type for user permissions, replace `any[]` with that type
  }

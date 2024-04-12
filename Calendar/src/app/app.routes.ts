import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { LoginErrorComponent } from './login-error/login-error.component';
import { DashboardComponent } from './dashboard/dashboard.component';

export const routes: Routes = [
    {path: `login`, component: LoginComponent},
    {path: `login-error`, component: LoginErrorComponent},
    {path: `dashboard`, component: DashboardComponent},
    {path: ``, component: LoginComponent},
];

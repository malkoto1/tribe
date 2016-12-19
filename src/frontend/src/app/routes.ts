import { RouterModule } from '@angular/router'
import { ModuleWithProviders } from '@angular/core'

import { MainContainer, HomeContainer } from './containers';

export const routes: ModuleWithProviders
    = RouterModule.forRoot([
        {
            path: 'home',
            component: HomeContainer
        },
        {
            path: 'products',
            component: HomeContainer
        },
        {
            path: '**',
            redirectTo: 'home'
        }
    ])
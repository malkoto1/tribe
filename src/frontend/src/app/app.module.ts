import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule } from '@angular/http';

import {
  App,
  routes
} from './';

import {
  MainContainer,
  HomeContainer
} from './containers'

import {
  Topbar,
  SideNavbar,
  Footer,
  CardGadget,
  LineChartGadget
} from './ui';

import { ApiService } from './services/api.service'

@NgModule({
  imports: [
    BrowserModule,
    routes,
    HttpModule
  ],
  declarations: [
    App,
    MainContainer,
    HomeContainer,
    Topbar,
    SideNavbar,
    Footer,
    CardGadget,
    LineChartGadget
  ],
  providers: [
    ApiService
  ],
  bootstrap: [App]
})
export class AppModule { }

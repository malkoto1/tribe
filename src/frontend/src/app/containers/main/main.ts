import { Component } from '@angular/core';

@Component({
    selector: 'main-container',
    template: `
        <div class="row main">
            <side-navbar class="col-md-2 col-lg-2"></side-navbar>
            <topbar class="col-md-10 col-lg-10"></topbar>
            <div class="main-container col-md-10 col-md-10">
                <router-outlet></router-outlet>
            </div>
        </div>
    `,
    styles: [`
        .main, side-navbar {
            height: 100%;
            margin-right: 0;
        }
        side-navbar {
            padding-right: 0;
        }
        topbar {
            padding-left: 0;
            padding-right: 0;
        }
        .main-container {
            padding: 15px;
        }
    `]
})

export class MainContainer {

}
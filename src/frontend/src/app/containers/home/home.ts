import { Component, OnInit } from '@angular/core';
import { ApiService } from './../../services/api.service'

@Component({
    selector: 'home-container',
    templateUrl: './home.html'
})

export class HomeContainer implements OnInit {
    items: any;

    constructor(private apiService: ApiService) {

    }

    ngOnInit(): void {
        this.apiService.get('items')
            .subscribe(items => {
                this.items = items;
            })
    }
}
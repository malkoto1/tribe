import {
    Component,
    Input
} from '@angular/core';

@Component({
    selector: 'card-gadget',
    templateUrl: './card-gadget.html',
    styleUrls: ['./card-gadget.css']
})

export class CardGadget {
    @Input()
    title: string;

    @Input()
    color: string;

    @Input()
    icon: string;

    @Input()
    data: string;
}
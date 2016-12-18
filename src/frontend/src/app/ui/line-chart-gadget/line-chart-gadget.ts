import {
    Component,
    ElementRef,
    ViewChild,
    OnInit
} from '@angular/core';

declare var Chart: any;

@Component({
    selector: 'line-chart-gadget',
    templateUrl: './line-chart-gadget.html',
    styleUrls: [
        './line-chart-gadget.css'
    ]
})

export class LineChartGadget implements OnInit {
    @ViewChild('myLineChart') myLineChart: ElementRef

    data = {
    labels: ["January", "February", "March", "April", "May", "June", "July"],
    datasets: [
        {
            label: "My First dataset",
            fill: false,
            lineTension: 0.1,
            backgroundColor: "rgba(75,192,192,0.4)",
            borderColor: "rgba(75,192,192,1)",
            borderCapStyle: 'butt',
            borderDashOffset: 0.0,
            borderJoinStyle: 'miter',
            pointBorderColor: "rgba(75,192,192,1)",
            pointBackgroundColor: "#fff",
            pointBorderWidth: 1,
            pointHoverRadius: 5,
            pointHoverBackgroundColor: "rgba(75,192,192,1)",
            pointHoverBorderColor: "rgba(220,220,220,1)",
            pointHoverBorderWidth: 2,
            pointRadius: 1,
            pointHitRadius: 10,
            data: [65, 59, 80, 81, 56, 55, 40],
            spanGaps: false,
        }
    ]
};

ngOnInit(): void {
    new Chart(this.myLineChart.nativeElement, {
        type: 'line',
        data: this.data
    })
}
}
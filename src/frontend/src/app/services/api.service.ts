import { Injectable } from '@angular/core'
import {
    Http,
    Response,
    Headers,
} from '@angular/http'

import { Observable } from 'rxjs/Rx'

@Injectable()
export class ApiService {
    private baseUrl: string

    constructor(private http: Http) {
        this.baseUrl = 'http://localhost:5000/'
    }

    get(target: any): Observable<any> {
        return this.http.get(this.baseUrl + target)
            .map(this.extractData)
            .catch(this.handleError)
    }

    post(target: any, payload: any): Observable<any> {
        return this.http.post(this.baseUrl + target, payload)
            //.map(this.extractData)
            .catch(this.handleError)
    }

    private extractData(res: Response) {
        return res.json()
    }

    private handleError(error: any) {
        let errMsg = (error.message) ? error.message :
            error.status ? `${error.status} - ${error.statusText}` : 'Server error'
        console.error(errMsg) // log to console instead
        return Observable.throw(errMsg)
    }
}
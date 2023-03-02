import { Component, OnInit } from '@angular/core';

import { EchoService } from '@app/shared/echo.service';

@Component({
  selector: 'app-protected',
  templateUrl: './protected.component.html',
  styleUrls: ['./protected.component.css']
})
export class ProtectedComponent implements OnInit {

  messageFromBackend: string = "";

  constructor(
    private echoService: EchoService
  ) { }

  ngOnInit(): void {
    this.echoService.echo().subscribe(result => {
      this.messageFromBackend = result['message'];
    })
  }

}
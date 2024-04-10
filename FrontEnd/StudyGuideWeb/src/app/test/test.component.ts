import { Component } from '@angular/core';
import { DataService } from '../data.service';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrl: './test.component.css'
})
export class TestComponent {
  constructor(private dataService: DataService) {}

  textValue = '';
  wordCount = 0;

  validateWordCount(event: any): void {
    const words = event.target.value.split(/\s+/);
    this.wordCount = words.filter((word: string) => word.length > 0).length;
  }

  submitForm(): void {
    console.log('Submitted:', this.textValue);
    // Here, you can handle the form submission, like sending the text to a server.
    this.dataService.submitForm(this.textValue).subscribe(data => {
      this.textValue = data.content
    })
  }

}

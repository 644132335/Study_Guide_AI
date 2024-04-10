import { Component } from '@angular/core';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrl: './test.component.css'
})
export class TestComponent {
  textValue = '';
  wordCount = 0;

  validateWordCount(event: any): void {
    const words = event.target.value.split(/\s+/);
    this.wordCount = words.filter((word: string) => word.length > 0).length;
  }

  submitForm(): void {
    console.log('Submitted:', this.textValue);
    // Here, you can handle the form submission, like sending the text to a server.
  }

}

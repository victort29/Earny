import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
questions = [
  {
    question:"this is a question",
    answer:""
  }
]

currentIndex = 0

  title = 'Earny';
  question = "Let's start with your age"

  addInput(answer: string){
    let lastquestion = this.questions[this.questions.length-1]

    lastquestion.answer = answer

    this.askQuestion();
  }

  askQuestion(){
    this.questions.push({question:"This is a new question", answer:""})
  }
}


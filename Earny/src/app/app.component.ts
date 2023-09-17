import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  questions =[
    "Hello! To provide you with the best investment advice, please tell me your age.",
    "At what age do you expect to need money for retirement?",
    "What is your expected net annual income?"
  ]
  
responses = [
  {
    question:this.questions[0],
    answer:""
  }
]

currentIndex = 0

  title = 'Earny';
  question = "Let's start with your age"

  addInput(answer: string){
    let lastquestion = this.responses[this.currentIndex]

    lastquestion.answer = answer

    this.askQuestion();
  }

  askQuestion(){
    this.currentIndex++;
    this.responses.push({question:this.questions[this.currentIndex], answer:""})
  }
}


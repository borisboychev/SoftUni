function solveClasses() {
  class Developer {
    constructor(firstName, lastName) {
      this.firstName = firstName;
      this.lastName = lastName;
      this.baseSalary = 1000;
      this.tasks = [];
      this.experience = 0;
    }

    addTask(id, taskName, priority) {
      let currentTask = {
        id,
        taskName,
        priority,
      };

      if (priority === "high") {
        this.tasks.push(currentTask, 0);
      } else {
        this.tasks.unshift(currentTask);
      }
      return `Task id ${id}, with ${priority} priority, has been added.`;
    }

    doTask() {
      if (this.tasks.length === 0) {
        return `${this.firstName}, you have finished all your tasks. You can rest now.`;
      }

      let taskDone = this.tasks.pop(0);
      return taskDone.taskName;
    }

    getSalary() {
      return `${this.firstName} ${this.lastName} has a salary of: ${this.baseSalary}`;
    }

    reviewTasks() {
      let result = "Tasks that need to be completed:";

      this.tasks.forEach((task) => {
        result += "\n";
        result += `${task.id}: ${task.taskName} - ${task.priority}`;
      });

      return result;
    }
  }

  class Junior extends Developer {
    constructor(firstName, lastName, bonus, experience) {
      super(firstName, lastName);
      this.baseSalary = 1000 + bonus;
      this.tasks = [];
      this.experience = experience;
    }

    learn(years) {
      this.experience += years;
    }
  }

  class Senior extends Developer {
    constructor(firstName, lastName, bonus, experience) {
      super(firstName, lastName);
      this.baseSalary = 1000 + bonus;
      this.tasks = [];
      this.experience = experience + 5;
    }

    changeTaskPriority(taskID) {
      let wantedTask = this.tasks.find((task) => task.id === taskID);
      this.tasks.pop(wantedTask);
      if (wantedTask.priority === "high") {
        wantedTask.priority = "low";
        this.tasks.push(wantedTask);
      } else {
        wantedTask.priority = "high";
        this.tasks.unshift(wantedTask);
      }
      return wantedTask;
    }
  }
  return {
    Developer,
    Junior,
    Senior,
  };
}
// let classes = solveClasses();
// const developer = new classes.Developer("George", "Joestar");
// console.log(developer.addTask(1, "Inspect bug", "low"));
// console.log(developer.addTask(2, "Update repository", "high"));
// console.log(developer.reviewTasks());
// console.log(developer.getSalary());
// const junior = new classes.Junior("Jonathan", "Joestar", 200, 2);
// console.log(junior.getSalary());
// const senior = new classes.Senior("Joseph", "Joestar", 200, 2);
// senior.addTask(1, "Create functionality", "low");
// senior.addTask(2, "Update functionality", "high");
// console.log(senior.changeTaskPriority(1)["priority"]);

//Zero test 1 Developer

let classes = solveClasses();
const developer = new classes.Developer("Jonathan", "Joestar");

// Salary
console.log(developer.getSalary());

// Add task
console.log(developer.addTask(1, "Inspect bug", "low"));

// Review tasks
console.log(developer.addTask(2, "Update repository", "high"));
console.log(developer.reviewTasks());

console.log(developer.doTask());
console.log(developer.doTask());
console.log(developer.doTask());

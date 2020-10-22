function solveClasses() {
  class Pet {
    constructor(owner, name) {
      this.owner = owner;
      this.name = name;
      this.comments = [];
    }

    addComment(comment) {
      if (this.comments.includes(comment)) {
        return "This comment is already added!";
      }
      this.comments.push(comment);
      return "Comment is added.";
    }

    feed() {
      return `${this.name} is fed`;
    }

    toString() {
      let result = `Here is ${this.owner}'s pet ${this.name}.`;

      if (this.comments.length > 0) {
        result += "\nSpecial requirements: ";
        result += this.comments.join(", ");

        return result;
      }
      return `Here is ${this.owner}'s pet ${this.name}.`;
    }
  }
  class Cat extends Pet {
    constructor(owner, name, insideHabits, scratching) {
      super(owner, name);
      this.insideHabits = insideHabits;
      this.scratching = scratching;
    }

    feed() {
      return super.feed() + ", happy and purring.";
    }

    toString() {
      let result = `\nMain information:\n${this.name} is a cat with ${this.insideHabits}`;
      if (this.scratching) {
        return super.toString() + result + ", but beware of scratches.";
      }

      return super.toString() + result + ".";
    }
  }

  class Dog extends Pet {
    constructor(owner, name, runningNeeds, trainability) {
      super(owner, name);
      this.runningNeeds = runningNeeds;
      this.trainability = trainability;
    }

    feed() {
      return super.feed() + ", happy and wagging tail.";
    }

    toString() {
      let result = `\nMain information:\n${this.name} is a dog with need of ${this.runningNeeds}km running every day and ${this.trainability} trainability.`;

      return super.toString() + result;
    }
  }

  return {
    Pet,
    Cat,
    Dog,
  };
}

let classes = solveClasses();
let pet = new classes.Pet("Ann", "Merry");
console.log(pet.addComment("likes bananas"));
console.log(pet.addComment("likes sweets"));
console.log(pet.feed());
console.log(pet.toString());

let cat = new classes.Cat("Jim", "Sherry", "very good habits", true);
console.log(cat.addComment("likes to be brushed"));
console.log(cat.addComment("sleeps a lot"));
console.log(cat.feed());
console.log(cat.toString());

let dog = new classes.Dog("Susan", "Max", 5, "good");
console.log(dog.addComment("likes to be brushed"));
console.log(dog.addComment("sleeps a lot"));
console.log(dog.feed());
console.log(dog.toString());

// const pet = new Pet("Boris", "Morgana");

// console.log(pet.addComment("juvala javala"));
// console.log(pet.addComment("asd"));
// console.log(pet.toString());

// const cat = new Cat("Boris", "Morgana", "sleeping", true);
// console.log(cat.feed());
// console.log(cat.toString());
// console.log("----------------------------------------------------");
// const dog = new Dog("Boris", "aira", "eating", "ready");
// console.log(dog.feed());
// console.log(dog.toString());

class Person {
  //private
  #currentAge;

  constructor(name, age = 20) {
    this.name = name;
    this.#currentAge = age;
  }

  set age(value) {
    if (value <= 0 || value >= 120) {
      throw Error("Invalid age");
    } else {
      this.#currentAge = value;
    }
  }

  get age() {
    return this.#currentAge;
  }

  greet() {
    console.log(
      "Hello, my name is " + this.name + " I am " + this.age + " years old"
    );
  }
}

let person = new Person("Boris");

console.log(person.age);
//console.log(person.#currentAge);

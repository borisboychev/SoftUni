class Parking {
  constructor(capacity) {
    this.capacity = capacity;
    this.vehicles = [];
  }

  addCar(carModel, carNumber) {
    if (this.vehicles.length >= this.capacity) {
      throw new Error("Not enough parking space.");
    }

    let currentCar = {
      carModel,
      carNumber,
      payed: false,
    };

    this.vehicles.push(currentCar);
    return `The ${carModel}, with a registration number ${carNumber}, parked.`;
  }

  removeCar(carNumber) {
    let currentCar = this.vehicles.find((v) => v.carNumber === carNumber);

    if (!currentCar) {
      throw new Error("The car, you're looking for, is not found.");
    }

    if (currentCar.payed == false) {
      throw new Error(
        `${currentCar.carNumber} needs to pay before leaving the parking lot.`
      );
    } else {
      this.vehicles.pop(currentCar);
      return `${carNumber} left the parking lot.`;
    }
  }

  pay(carNumber) {
    let currentCar = this.vehicles.find((v) => v.carNumber === carNumber);

    if (!currentCar) {
      throw new Error(`${carNumber} is not in the parking lot.`);
    }
    if (currentCar.payed) {
      throw new Error(`${carNumber}'s driver successfully payed for his stay.`);
    } else {
      currentCar.payed = true;
      return `${carNumber}'s driver successfully payed for his stay.`;
    }
  }

  getStatistics(carNumber = null) {
    let result = "";
    //no parameter passed
    if (carNumber === null) {
      let emptySlots = this.capacity - this.vehicles.length;
      result = `The Parking Lot has ${emptySlots} empty spots left.`;

      this.vehicles = this.vehicles.sort((a, b) =>
        a.carModel.localeCompare(b.carModel)
      );
      this.vehicles.foreach((car) => {
        result += "\n";
        result += `${car.carModel} == ${car.carNumber} - ${
          car.payed ? "Has payed" : "Not payed"
        }`;
      });
    } else {
      let currentCar = this.vehicles.find((v) => v.carNumber === carNumber);
      result = `${currentCar.carModel} == ${carNumber} - ${
        currentCar.payed ? "Has payed" : "Not payed"
      }`;
    }
    return result;
  }
}

const parking = new Parking(12);

console.log(parking.addCar("Aolvo t600", "TX3691CA"));
console.log(parking.addCar("Aolvo b600", "TX3691CB"));

console.log(parking.pay("TX3691CA"));

console.log(parking.getStatistics("TX3691CB"));

class VeterinaryClinic {
  clients = [];
  constructor(clinicName, capacity) {
    this.clinicName = clinicName;
    this.capacity = capacity;
    this.totalProfit = 0;
    this.currentWorkload = 0;
  }

  newCustomer(ownerName, petName, kind, procedures) {
    if (this.currentWorkload >= this.capacity) {
      throw new Error("Sorry, we are not able to accept more patients!");
    }

    //check if pet is currnetly in the clinic with procedures
    //"This pet is already registered under { ownerName } name! { petName } is on our lists, waiting for { all his procedures separated by ', ' }."
    let currentOwner = this.clients.find((x) => x.ownerName === ownerName);

    if (currentOwner && currentOwner.pets.some((p) => p.petName === petName)) {
      let pet = currentOwner.pets.find((p) => p.petName === petName);

      if (pet.procedures.length > 0) {
        throw new Error(
          `This pet is already registered under ${
            currentOwner.ownerName
          } name! ${
            pet.petName
          } is on our lists, waiting for ${pet.procedures.join(", ")}.`
        );
      } else {
        pet.procedures = procedures;
      }
      //check if client is registered
    } else if (!currentOwner) {
      //add new client
      currentOwner = {
        ownerName: ownerName,
        pets: [],
      };
      this.clients.push(currentOwner);
    }

    //add pet to owner
    currentOwner.pets.push({
      petName: petName,
      kind: kind,
      procedures: procedures,
    });

    //modify worload
    this.currentWorkload++;

    return `Welcome ${petName}!`;
  }

  onLeaving(ownerName, petName) {
    let currentOwner = this.clients.find((x) => x.ownerName === ownerName);
    let currentPet = currentOwner.pets.find((p) => p.petName === petName);

    if (!currentOwner) {
      throw new Error("Sorry, there is no such client!");
    }

    if (!currentPet || currentPet.procedures.length == 0) {
      throw new Error(`Sorry, there are no procedures for ${petName}!`);
    }

    this.totalProfit += 500 * currentPet.procedures.length;
    currentPet.procedures = [];
    this.currentWorkload--;

    return `Goodbye ${petName}. Stay safe!`;
  }

  toString() {
    let busyPercent = Math.floor((this.currentWorkload / this.capacity) * 100);
    let result = `${this.clinicName} is ${busyPercent}% busy today!`;
    result += "\n";
    result += `Total profit: ${this.totalProfit.toFixed(2)}$`;
    this.clients.sort((a, b) => a.ownerName.localeCompare(b.ownerName));

    for (const client of this.clients) {
      client.pets.sort((a, b) => a.petName.localeCompare(b.petName));
      result += "\n";
      result += `${client.ownerName} with:`;
      for (const pet of client.pets) {
        result += "\n";
        result += `---${pet.petName} - a ${
          pet.kind
        } that needs: ${pet.procedures.join(", ")}`;
      }
    }

    return result;
  }
}

let clinic = new VeterinaryClinic("SoftCare", 10);
console.log(
  clinic.newCustomer("Jim Jones", "Tom", "Cat", ["A154B", "2C32B", "12CDB"])
);
console.log(
  clinic.newCustomer("Anna Morgan", "Max", "Dog", ["SK456", "DFG45", "KS456"])
);
console.log(clinic.newCustomer("Jim Jones", "Tiny", "Cat", ["A154B"]));
console.log(clinic.onLeaving("Jim Jones", "Tiny"));
console.log(clinic.toString());
clinic.newCustomer("Jim Jones", "Sara", "Dog", ["A154B"]);
console.log(clinic.toString());

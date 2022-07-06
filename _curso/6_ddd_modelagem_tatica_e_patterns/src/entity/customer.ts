import Address from './value_objects/address';

export default class Customer {
    _id: string;
    _name: string;
    _address!: Address;

    constructor(id: string, name: string) {
        this._id = id;
        this._name = name;
    }

    changeName(name: string) {
        this._name = name;
        this.validate();
    }

    changeAddress(address: Address) {
        this._address = address;
        this.validate();
    }

    validate(): void {
        // Valida a entidade
    }

    set Address(address: Address) {
        this._address = address;
    }
}
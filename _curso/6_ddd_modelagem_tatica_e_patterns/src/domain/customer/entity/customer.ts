import Address from '../value_object/address';

export default class Customer {
    private _id: string;
    private _name: string;
    private _address!: Address;
    private _active: boolean = true;
    private _rewardPoints: number = 0;

    constructor(id: string, name: string) {
        this._id = id;
        this._name = name;
        this.validate();
    }

    get id(): string {
        return this._id;
    }

    get name(): string {
        return this._name;
    }

    get rewardPoints(): number {
        return this._rewardPoints;
    }

    set Address(address: Address) {
        this._address = address;
    }

    changeName(name: string): void {
        this._name = name;
        this.validate();
    }

    changeAddress(address: Address): void {
        this._address = address;
        this.validate();
    }

    activate(): void {
        if (this._address === undefined) {
            throw new Error("Address is mandatory to activate a customer");
        }

        this._active = true;
    }

    deactivate(): void {
        this._active = false;
    }

    isActive(): boolean {
        return this._active;
    }

    validate(): void {
        if (this._id.length === 0) {
            throw new Error("Id is required");
        }

        if (this._name.length === 0) {
            throw new Error("Name is required");
        }
    }

    addRewardPoints(points: number) {
        this._rewardPoints += points;
    }
}
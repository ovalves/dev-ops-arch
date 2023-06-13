import ProductFactory from './product.factory';

describe('Product factory unit test', () => {
    it('should create a product', () => {
        const product = ProductFactory.create('Product A', 15);

        expect(product.id).toBeDefined();
        expect(product.name).toBe('Product A');
        expect(product.price).toBe(15);
        expect(product.constructor.name).toBe('Product');
    });
});

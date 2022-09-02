import ValidatorInterface from '../../@shared/validator/validator.interface';
import Address from '../value-object/address';
import * as yup from 'yup';

export default class AddressYupValidator implements ValidatorInterface<Address> {
    validate(entity: Address): void {
        try {
            yup.object()
                .shape({
                    street: yup.string().required('Street is required'),
                    number: yup.string().required('Number is required'),
                    zip: yup.string().required('Zip is required'),
                    city: yup.string().required('City is required')
                })
                .validateSync(
                    {
                        street: entity.street,
                        number: entity.number,
                        zip: entity.zip,
                        city: entity.city,
                    },
                    {
                        abortEarly: false
                    }
                );
        } catch (errors) {
            const e = errors as yup.ValidationError;
            e.errors.forEach((error) => {
                entity.notification.addError({
                    context: 'address',
                    message: error
                });
            });
        }
    }
}

package gateway

import "eda-wallet/internal/entity"

type TransactionGateway interface {
	Create(transaction *entity.Transaction) error
}

# Café Calle Ocho – User Stories

## Persona 1: Customer
A customer who wants to browse the café menu, order food, and track an order.

## Persona 2: Kitchen Staff
A staff member who needs to view incoming orders and update their preparation status.

---

## Story 1: Browse Menu
**Priority:** MUST

As a customer, I want to browse the café menu so that I can see the available food and drinks.

**Acceptance Criteria**

1. Given that the customer opens the menu, when the menu loads, then the system displays available items with names and prices.
2. Given that the menu cannot load, when the customer opens it, then the system displays an error message and an option to try again.

## Story 2: View Food Item Details
**Priority:** SHOULD

As a customer, I want to view food item details so that I can understand what I am ordering.

**Acceptance Criteria**

1. Given that a food item is available, when the customer selects it, then the system displays its description and price.
2. Given that an item is unavailable, when the customer selects it, then the system displays an unavailable message and prevents the customer from adding it to the order.

## Story 3: Add Items to Order
**Priority:** MUST

As a customer, I want to add menu items to my order so that I can purchase the items I want.

**Acceptance Criteria**

1. Given that a menu item is available, when the customer selects Add to Order, then the item appears in the order summary.
2. Given that a menu item is unavailable, when the customer tries to add it, then the system displays an error and does not add the item.

## Story 4: Place an Order
**Priority:** MUST

As a customer, I want to submit my order so that the café can prepare my food.

**Acceptance Criteria**

1. Given that the order contains valid items, when the customer submits it, then the system creates the order and displays a confirmation.
2. Given that the order is empty, when the customer tries to submit it, then the system displays a message asking the customer to add an item.

## Story 5: Track Order Status
**Priority:** MUST

As a customer, I want to check my order status so that I know whether my food is being prepared or is ready.

**Acceptance Criteria**

1. Given that the customer has placed an order, when the customer views its status, then the system displays the current order status.
2. Given that the order number is invalid, when the customer searches for it, then the system displays a message that the order cannot be found.

## Story 6: View Kitchen Order Board
**Priority:** MUST

As a kitchen staff member, I want to view incoming orders so that I know which orders need preparation.

**Acceptance Criteria**

1. Given that customer orders have been submitted, when kitchen staff open the order board, then the system displays the active orders.
2. Given that no active orders exist, when kitchen staff open the order board, then the system displays a message stating that there are no active orders.

## Story 7: Start Preparing an Order
**Priority:** MUST

As a kitchen staff member, I want to mark an order as preparing so that the customer can see that work has started.

**Acceptance Criteria**

1. Given that an order is waiting, when kitchen staff select Start Preparing, then the order status changes to Preparing.
2. Given that an order does not exist or is already completed, when kitchen staff try to start preparation, then the system displays an error and does not change the status.

## Story 8: Mark Order Ready
**Priority:** SHOULD

As a kitchen staff member, I want to mark an order as ready so that the customer knows it is ready for pickup.

**Acceptance Criteria**

1. Given that an order is being prepared, when kitchen staff select Mark Ready, then the order status changes to Ready.
2. Given that an order has not started preparation, when kitchen staff try to mark it ready, then the system displays an error and does not change the status.

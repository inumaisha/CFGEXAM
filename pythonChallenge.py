#calculate the initial number of classes
#calculate the number of students per class
#allocate students to classes
#print "Proposed Allocation:", proposed_classes, "classes"
#print allocation.

def allocate_classes(num_students):
    max_class_size = 30
    min_classes = 2

    num_classes = min((num_students + max_class_size - 1) // max_class_size, min_classes)

    base_allocation, remaining_students = divmod(num_students, num_classes)
    
    allocation = {f'Class {i}': base_allocation for i in range(1, num_classes + 1)}

    for i in range(1, remaining_students + 1):
        allocation[f'Class {i}'] += 1

    print(f'Proposed Allocation: {num_classes} classes')
    print(allocation)

#examples from question
allocate_classes(31)
allocate_classes(59)
allocate_classes(87)

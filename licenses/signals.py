from django.db.models.signals import post_save
from django.dispatch import receiver
from contracts.models import Contract
from .models import License

@receiver(post_save, sender=License)
def update_outstanding_amount(sender, instance, **kwargs):
    contract_instance = Contract.objects.get(pk=instance.contract_id)
    if instance.renewal_status == 'Paid':
        contract_instance.amount_outstanding = contract_instance.total_value - instance.current_cost
    print('Amount Outstanding:',contract_instance.amount_outstanding)
    print('Total Value:',contract_instance.total_value)
    print('License Value:',instance.current_cost)
    contract_instance.save()
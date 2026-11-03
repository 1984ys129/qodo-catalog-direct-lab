"""Catalog client using the shared SDK transport boundary."""

from catalog.sdk import fetch_product


def load_product(transport, tenant, sku):
    return fetch_product(transport, sku=sku, tenant=tenant)

from fastapi import APIRouter

from . import assessment_router
# from . import entity_router
# from . import project_segment_router
# from . import customer_router
# from . import area_router
# from . import currency_router
# from . import brand_router
# from . import product_category_router
# from . import competitor_router
# from . import opportunity_router
# from . import customer_segment_router
# from . import term_and_condition_router
# from . import customer_response_router
# from . import customer_group_router
# from . import surface_router
# from . import task_type_router
# from . import staff_routers
# from . import source_router
# from . import series_router
# from . import opportunity_sharing_master_router
# from . import product_type_router
# from . import public_holiday_router
# from . import smp_update_router
# from . import opportunity_status_router
# from . import designation_router
# from . import non_standard_item_router
# from . import location_router
# from . import cut_tile_router
# from . import department_router
# from . import division_router
# from . import country_router
# from . import quotation_router
# from . import lead_router
# from . import walkin_router
# from . import tier_router
# from . import tax_explanation_router
# from . import tax_area_router
# from . import payment_term_router
# from . import region_router
# from . import customer_ranking_router
# from . import nature_of_business_router
# from . import sales_team_router
# from . import campaign_router
# from . import sales_planner_router
# from . import sales_activity_router
# from . import gl_class_router
# from . import customer_acknowledgement_router
# from . import task_router
# from . import customer_type_router
# from . import customer_price_group_router
# from . import fail_reason_router
# from . import port_of_loading_router
# from . import collection_manager_router
# from . import credit_manager_router
# from . import price_exception_router
# from . import search_type_router
# from . import parent_number_router
# from . import customer_invoice_to_router
# from . import customer_statement_to_router
# from . import business_unit_router
# from . import tile_thickness_router
# from . import delinquency_policy_type_router
# from . import base_tile_router
# from . import shipping_term_router
# from . import product_status_router
# from . import approval_router
# from . import audit_tracking_router
# from . import credit_message_router
# from . import intercompany_router
# from . import attachment_route
# from . import demand_forecast_router
# from . import approval_customer_router
# from . import smp_request_router

api_router = APIRouter()
api_router.include_router(assessment_router.router)
# api_router.include_router(entity_router.router)
# api_router.include_router(project_segment_router.router)
# api_router.include_router(customer_router.router)
# api_router.include_router(area_router.router)
# api_router.include_router(currency_router.router)
# api_router.include_router(brand_router.router)
# api_router.include_router(product_category_router.router)
# api_router.include_router(competitor_router.router)
# api_router.include_router(opportunity_router.router)
# api_router.include_router(customer_segment_router.router)
# api_router.include_router(term_and_condition_router.router)
# api_router.include_router(customer_response_router.router)
# api_router.include_router(customer_group_router.router)
# api_router.include_router(surface_router.router)
# api_router.include_router(task_type_router.router)
# api_router.include_router(staff_routers.router)
# api_router.include_router(source_router.router)
# api_router.include_router(series_router.router)
# api_router.include_router(opportunity_sharing_master_router.router)
# api_router.include_router(product_type_router.router)
# api_router.include_router(public_holiday_router.router)
# api_router.include_router(smp_update_router.router)
# api_router.include_router(opportunity_status_router.router)
# api_router.include_router(designation_router.router)
# api_router.include_router(non_standard_item_router.router)
# api_router.include_router(location_router.router)
# api_router.include_router(cut_tile_router.router)
# api_router.include_router(department_router.router)
# api_router.include_router(division_router.router)
# api_router.include_router(country_router.router)
# api_router.include_router(quotation_router.router)
# api_router.include_router(lead_router.router)
# api_router.include_router(walkin_router.router)
# api_router.include_router(tier_router.router)
# api_router.include_router(tax_explanation_router.router)
# api_router.include_router(tax_area_router.router)
# api_router.include_router(payment_term_router.router)
# api_router.include_router(region_router.router)
# api_router.include_router(customer_ranking_router.router)
# api_router.include_router(nature_of_business_router.router)
# api_router.include_router(sales_team_router.router)
# api_router.include_router(campaign_router.router)
# api_router.include_router(sales_planner_router.router)
# api_router.include_router(sales_activity_router.router)
# api_router.include_router(gl_class_router.router)
# api_router.include_router(customer_acknowledgement_router.router)
# api_router.include_router(task_router.router)
# api_router.include_router(customer_type_router.router)
# api_router.include_router(customer_price_group_router.router)
# api_router.include_router(task_type_router.router)
# api_router.include_router(product_router.router)
# api_router.include_router(collection_manager_router.router)
# api_router.include_router(fail_reason_router.router)
# api_router.include_router(port_of_loading_router.router)
# api_router.include_router(credit_manager_router.router)
# api_router.include_router(price_exception_router.router)
# api_router.include_router(search_type_router.router)
# api_router.include_router(parent_number_router.router)
# api_router.include_router(customer_invoice_to_router.router)
# api_router.include_router(customer_statement_to_router.router)
# api_router.include_router(business_unit_router.router)
# api_router.include_router(tile_thickness_router.router)
# api_router.include_router(delinquency_policy_type_router.router)
# api_router.include_router(base_tile_router.router)
# api_router.include_router(shipping_term_router.router)
# api_router.include_router(product_status_router.router)
# api_router.include_router(approval_router.router)
# api_router.include_router(audit_tracking_router.router)
# api_router.include_router(credit_message_router.router)
# api_router.include_router(intercompany_router.router)
# api_router.include_router(attachment_route.router)
# api_router.include_router(demand_forecast_router.router)
# api_router.include_router(approval_customer_router.router)
# api_router.include_router(approval_customer_router.routerMatrix)
# api_router.include_router(smp_request_router.router)


import pytest
from pages.price_calculator_page import PriceCalcPage
from pages.email_page import EmailPage
from pages.locators import PriceCalcPageLocators as locator


class TestCalculateComputeEngine:
    SECTION_NAME = 'Compute Engine'

    @pytest.mark.skip
    @pytest.mark.parametrize("number_of_instances, OS, machine_class, machine_series, machine_type, ssd_option, gpu_model, gpu_count, datacenter_location, committed_usage, expected_total_cost", 
    [(4, 'Free', 'Regular', 'N1', 'n1-standard-8', '2x375', 'NVIDIA Tesla T4', 1, 'Frankfurt', '1 Year', '1,841.97')])
    def test_calculate_compute_engine_costs(self, browser, number_of_instances, OS, machine_class, machine_series, machine_type, ssd_option, gpu_model, gpu_count, datacenter_location, committed_usage, expected_total_cost):
        price_calc_page = PriceCalcPage(browser=browser)
        price_calc_page.open()
        price_calc_page.activate_section(section=TestCalculateComputeEngine.SECTION_NAME)
        price_calc_page.input_num_of_instances(number_of_instances=number_of_instances)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_OS, option_to_choose=OS)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_MACHINE_CLASS, option_to_choose=machine_class)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_MACHINE_SERIES, option_to_choose=machine_series)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_MACHINE_TYPE, option_to_choose=machine_type)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_SSD, option_to_choose=ssd_option)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_DATACENTER_LOCATION, option_to_choose=datacenter_location)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_COMMITTED_USAGE, option_to_choose=committed_usage)
        price_calc_page.select_gpu(gpu_type=gpu_model, gpu_quantity=gpu_count)
        price_calc_page.submit_calculation()
        price_calc_page.verify_item_in_estimate_section(locator=locator.ESTIMATE_SECTION_COMMITTED_USAGE, expected_option=committed_usage)
        price_calc_page.verify_item_in_estimate_section(locator=locator.ESTIMATE_SECTION_DATACENTER_LOCATION, expected_option=datacenter_location)
        price_calc_page.verify_item_in_estimate_section(locator=locator.ESTIMATE_SECTION_MACHINE_CLASS, expected_option=machine_class)
        price_calc_page.verify_item_in_estimate_section(locator=locator.ESTIMATE_SECTION_MACHINE_TYPE, expected_option=machine_type)
        price_calc_page.verify_item_in_estimate_section(locator=locator.ESTIMATE_SECTION_SSD, expected_option=ssd_option)
        price_calc_page.verify_item_in_estimate_section(locator=locator.ESTIMATE_SECTION_TOTAL_COST, expected_option=expected_total_cost)


    @pytest.mark.usefixtures('browser2')
    @pytest.mark.parametrize("number_of_instances, OS, machine_class, machine_series, machine_type, ssd_option, gpu_model, gpu_count, datacenter_location, committed_usage, expected_total_cost", 
    [(4, 'Free', 'Regular', 'N1', 'n1-standard-8', '2x375', 'NVIDIA Tesla T4', 1, 'Frankfurt', '1 Year', '1,841.97')])
    def test_calculate_compute_engine_costs_with_email_verification(self, browser, browser2, number_of_instances, OS, machine_class, machine_series, machine_type, ssd_option, gpu_model, gpu_count, datacenter_location, committed_usage, expected_total_cost):
        price_calc_page = PriceCalcPage(browser=browser)
        price_calc_page.open()
        price_calc_page.activate_section(section=TestCalculateComputeEngine.SECTION_NAME)
        price_calc_page.input_num_of_instances(number_of_instances=number_of_instances)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_OS, option_to_choose=OS)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_MACHINE_CLASS, option_to_choose=machine_class)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_MACHINE_SERIES, option_to_choose=machine_series)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_MACHINE_TYPE, option_to_choose=machine_type)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_SSD, option_to_choose=ssd_option)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_DATACENTER_LOCATION, option_to_choose=datacenter_location)
        price_calc_page.select_option_from_md_dropdown(dropdown_selector=locator.COMPUTE_ENGINE_FORM_COMMITTED_USAGE, option_to_choose=committed_usage)
        price_calc_page.select_gpu(gpu_type=gpu_model, gpu_quantity=gpu_count)
        price_calc_page.submit_calculation()
        price_calc_page.verify_item_in_estimate_section(locator=locator.ESTIMATE_SECTION_COMMITTED_USAGE, expected_option=committed_usage)
        price_calc_page.verify_item_in_estimate_section(locator=locator.ESTIMATE_SECTION_DATACENTER_LOCATION, expected_option=datacenter_location)
        price_calc_page.verify_item_in_estimate_section(locator=locator.ESTIMATE_SECTION_MACHINE_CLASS, expected_option=machine_class)
        price_calc_page.verify_item_in_estimate_section(locator=locator.ESTIMATE_SECTION_MACHINE_TYPE, expected_option=machine_type)
        price_calc_page.verify_item_in_estimate_section(locator=locator.ESTIMATE_SECTION_SSD, expected_option=ssd_option)
        price_calc_page.verify_item_in_estimate_section(locator=locator.ESTIMATE_SECTION_TOTAL_COST, expected_option=expected_total_cost)
        email_page = EmailPage(browser=browser2)
        email_page.open()
        email_page.open_new_email_inbox()
        price_calc_page.email_estimate(email_address=email_page.get_email_address())
        email_page.wait_for_email()
        email_page.verify_emailed_monthly_costs(expected_monthly_cost=expected_total_cost)

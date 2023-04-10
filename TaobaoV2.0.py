# -*- coding = utf-8 -*-
# @Time : 2022/11/1 15:03
# @Author : sksk
# @File : TaobaoV2.0.py
# @Software : PyCharm

import time
import datetime
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


def get_curr_strftime():
    """
    获取当前时间, 并格式化
    :return: 格式化的当前时间
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def find_element_if_exists(by, ele):
    """
    查找元素是否存在
    :param by: selenium By对象
    :param ele: element元素
    :return: 若存在返回True 存在返回False
    """
    try:
        if driver.find_element(by, ele):
            return True
    except NoSuchElementException:
        return False
    return False


def login():
    """
    登录功能
    :return: 登录成功返回True 登录失败返回False
    """
    driver.get("https://www.taobao.com")
    time.sleep(2)
    if find_element_if_exists(By.CSS_SELECTOR, '#J_SiteNavLogin > div.site-nav-menu-hd > div > '
                                               'a.site-nav-login-info-nick '):
        print("已登录")
        return True
    if find_element_if_exists(By.LINK_TEXT, "亲，请登录"):
        driver.find_element(By.LINK_TEXT, "亲，请登录").click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, "//*[@id=\"login\"]/div[1]/i").click()
        print("请在两分钟内使用淘宝完成扫码登录")
        # 检测是否已登录
        for i in range(60):
            if find_element_if_exists(By.CSS_SELECTOR,
                                      '#J_SiteNavLogin > div.site-nav-menu-hd > div > a.site-nav-login-info-nick '):
                print("已登录")
                return True
            else:
                # 每两秒检测一次，总共检测60次
                time.sleep(2)
    return False


def start_shopping(check_goods):
    """
    开始抢购
    :param check_goods: 需要勾选的物品
    :return: 抢购成功返回True 失败返回False
    """
    print("开始抢购")
    # 刷新页面
    driver.refresh()
    # 勾选商品
    driver.implicitly_wait(1)
    checked_count = checked_goods(check_goods)
    if checked_count > 0:
        if submit_order(By.XPATH, "//*[@class=\"submit-btn\"]"):
            print("结算成功，时间：", get_curr_strftime())
            print("开始提交订单")
            # 提交订单
            if submit_order(By.XPATH, "//*[@id=\"submitOrderPC_1\"]/div[1]/a[2]"):
                print("提交订单成功")
            return True
        else:
            print("结算失败")
    else:
        print('未成功勾选任何商品')
    return False


def checked_goods(check_goods):
    """
    勾选购物车商品
    :param check_goods: 需勾选商品勾选框的xpath定位 (数组)
    :return: 成功勾选商品的数量
    """
    count = 0
    for g in check_goods:
        if find_element_if_exists(By.XPATH, g):
            checkbox = driver.find_element(By.XPATH, g)
            driver.execute_script("arguments[0].click();", checkbox)
            count += 1
        else:
            print("未找到商品", g, "的勾选框，跳过勾选该商品")
    print(f"已勾选{count}件商品")
    return count


def submit_order(by, ele):
    """
    点击按钮
    :param by: selenium by 对象
    :param ele: 按钮的XPATH
    :return: 点击成功返回True 失败返回False
    """
    for i in range(50):
        try:
            print(f"执行第{i+1}次点击")
            if find_element_if_exists(by, ele):
                btn = driver.find_element(by, ele)
                driver.execute_script("arguments[0].click();", btn)
                print("点击成功")
                return True
            time.sleep(0.01)
        except NoSuchElementException:
            print(f"未找到元素{ele}")
            time.sleep(0.01)
        except:
            print("发生未知异常")
            break
    return False


if __name__ == '__main__':
    # 抢购时间
    buy_time = "2023-06-18 00:00:00"
    # 抢购商品 (商品勾选框的xpath)
    goods = ['//*[@id="J_Order_s_906788779_1"]/div[1]/div/div/label']
    driver = webdriver.Chrome()
    # 全屏显示
    driver.maximize_window()
    if login():
        print("登录成功，开始准备抢购")
        if find_element_if_exists(By.XPATH, "//*[@id=\"J_MiniCart\"]/div[1]/a/span[2]"):
            driver.find_element(By.XPATH, "//*[@id=\"J_MiniCart\"]/div[1]/a/span[2]").click()
            while True:
                curr_time = get_curr_strftime()  # 获取当前时间
                if curr_time < buy_time:
                    print("抢购时间未到，当前时间：" + curr_time)
                    time.sleep(0.01)
                    continue
                start_time = time.time()
                if start_shopping(goods):
                    elapsed_time = round(float(time.time() - start_time), 2)  # 计算耗时
                    print(f"抢购成功！！！耗时：{elapsed_time}秒")
                    driver.execute_script(f"alert('抢购成功啦！！！耗时{elapsed_time}秒')")
                    break
                else:
                    print("抢购失败，重新开始")
                    driver.execute_script("alert('抢购失败，重新开始TvT')")
                    time.sleep(1)
        else:
            print("未找到购物车按钮TvT")
    else:
        # 关闭浏览器
        driver.close()
        print("登录失败")


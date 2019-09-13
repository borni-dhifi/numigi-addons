FROM quay.io/numigi/odoo-public:12.latest
MAINTAINER numigi <contact@numigi.com>

USER root

COPY .docker_files/requirements.txt .
RUN pip3 install -r requirements.txt

USER odoo

COPY purchase_order_sending_state /mnt/extra-addons/purchase_order_sending_state
COPY stock_move_line_auto_fill /mnt/extra-addons/stock_move_line_auto_fill
COPY stock_user_access /mnt/extra-addons/stock_user_access

COPY .docker_files/main /mnt/extra-addons/main
COPY .docker_files/odoo.conf /etc/odoo

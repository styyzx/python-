/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50726
 Source Host           : localhost:3306
 Source Schema         : tushare

 Target Server Type    : MySQL
 Target Server Version : 50726
 File Encoding         : 65001

 Date: 17/11/2021 17:04:54
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for stock_daily_find2
-- ----------------------------
DROP TABLE IF EXISTS `stock_daily_find2`;
CREATE TABLE `stock_daily_find2` (
  `ts_code` varchar(10) NOT NULL COMMENT '股票代码',
  `trade_date` date NOT NULL COMMENT '交易日期',
  `open` double DEFAULT NULL COMMENT '开盘价',
  `high` double DEFAULT NULL COMMENT '最高价',
  `low` double DEFAULT NULL COMMENT '最低价',
  `close` double DEFAULT NULL COMMENT '收盘价',
  `pre_close` double DEFAULT NULL COMMENT '昨日收盘价',
  `change` double DEFAULT NULL COMMENT '涨跌额',
  `pct_chg` double DEFAULT NULL COMMENT '涨跌幅',
  `vol` double DEFAULT NULL COMMENT '成交量 （手）',
  `amount` double DEFAULT NULL COMMENT '成交额 （千元）',
  `turnover_rate` double DEFAULT NULL COMMENT '换手率',
  `volume_ratio` double DEFAULT NULL COMMENT '量比',
  `vol_925` double DEFAULT NULL COMMENT '925',
  `vol_925_ratio` double DEFAULT NULL COMMENT '量比2',
  `cur_time` datetime DEFAULT NULL,
  UNIQUE KEY `ts_code_date` (`ts_code`,`cur_time`) USING BTREE COMMENT '以股票代码和日期作为主键',
  KEY `ts_code` (`ts_code`) USING BTREE,
  KEY `trade_date` (`trade_date`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 ROW_FORMAT=DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;

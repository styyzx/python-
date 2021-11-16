/*
Navicat MySQL Data Transfer

Source Server         : 5.0local
Source Server Version : 50736
Source Host           : localhost:3306
Source Database       : tushare

Target Server Type    : MYSQL
Target Server Version : 50736
File Encoding         : 65001

Date: 2021-11-17 07:36:54
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for tdx_daily
-- ----------------------------
DROP TABLE IF EXISTS `tdx_daily`;
CREATE TABLE `tdx_daily` (
  `id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `code` varchar(20) DEFAULT NULL,
  `price` double DEFAULT NULL,
  `servertime` time DEFAULT NULL,
  `reversed_bytes3` double DEFAULT NULL,
  `vol` double DEFAULT NULL,
  `open` double DEFAULT NULL,
  `high` double DEFAULT NULL,
  `low` double DEFAULT NULL,
  `last_close` double DEFAULT NULL,
  `cur_vol` double DEFAULT NULL,
  `cur_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4;
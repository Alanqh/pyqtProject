/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80031 (8.0.31)
 Source Host           : localhost:3306
 Source Schema         : 动物识别系统

 Target Server Type    : MySQL
 Target Server Version : 80031 (8.0.31)
 File Encoding         : 65001

 Date: 30/03/2023 23:00:47
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for animals
-- ----------------------------
DROP TABLE IF EXISTS `animals`;
CREATE TABLE `animals`  (
  `A_ID` int NOT NULL AUTO_INCREMENT,
  `animal` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`A_ID`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 30 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of animals
-- ----------------------------
INSERT INTO `animals` VALUES (1, '老虎');
INSERT INTO `animals` VALUES (2, '金钱豹');
INSERT INTO `animals` VALUES (3, '长颈鹿');
INSERT INTO `animals` VALUES (4, '斑马');
INSERT INTO `animals` VALUES (5, '驼鸟');
INSERT INTO `animals` VALUES (6, '企鹅');
INSERT INTO `animals` VALUES (7, '海燕');
INSERT INTO `animals` VALUES (8, '兔子');
INSERT INTO `animals` VALUES (9, '猫');
INSERT INTO `animals` VALUES (10, '犀牛');
INSERT INTO `animals` VALUES (11, '熊猫');
INSERT INTO `animals` VALUES (12, '鹦鹉');
INSERT INTO `animals` VALUES (13, '鸭子');
INSERT INTO `animals` VALUES (14, '鹰');
INSERT INTO `animals` VALUES (15, '鸭子');
INSERT INTO `animals` VALUES (16, '鹅');
INSERT INTO `animals` VALUES (17, '鸦');
INSERT INTO `animals` VALUES (18, '鹰');
INSERT INTO `animals` VALUES (19, '鹦鹉');
INSERT INTO `animals` VALUES (20, '青蛙');
INSERT INTO `animals` VALUES (21, '蝾螈');
INSERT INTO `animals` VALUES (22, '蟾蜍');
INSERT INTO `animals` VALUES (23, '比目鱼');
INSERT INTO `animals` VALUES (24, '鲫鱼');
INSERT INTO `animals` VALUES (25, '蛇');
INSERT INTO `animals` VALUES (26, '壁虎');
INSERT INTO `animals` VALUES (27, '乌龟');
INSERT INTO `animals` VALUES (28, '玳瑁');
INSERT INTO `animals` VALUES (29, '鳄鱼');

SET FOREIGN_KEY_CHECKS = 1;

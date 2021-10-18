/*
 Navicat Premium Data Transfer

 Source Server         : Tencent
 Source Server Type    : MySQL
 Source Server Version : 50650
 Source Host           : 1.117.231.72:3306
 Source Schema         : books

 Target Server Type    : MySQL
 Target Server Version : 50650
 File Encoding         : 65001

 Date: 18/10/2021 21:19:20
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for book_details
-- ----------------------------
DROP TABLE IF EXISTS `book_details`;
CREATE TABLE `book_details`  (
  `id` bigint(20) UNSIGNED NOT NULL AUTO_INCREMENT,
  `book_id` int(10) UNSIGNED NOT NULL,
  `sort_id` int(10) UNSIGNED NOT NULL,
  `detail_title` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `detail_content` mediumtext CHARACTER SET utf8 COLLATE utf8_general_ci NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `book_id_index`(`book_id`) USING BTREE,
  INDEX `sort_id_index`(`sort_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1040720 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

-- ----------------------------
-- Table structure for book_infos
-- ----------------------------
DROP TABLE IF EXISTS `book_infos`;
CREATE TABLE `book_infos`  (
  `id` int(10) UNSIGNED NOT NULL AUTO_INCREMENT,
  `book_id` int(10) UNSIGNED NOT NULL,
  `book_cate` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `book_name` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `image_urls` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `book_author` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `book_status` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `book_last_update_time` datetime(0) NULL DEFAULT NULL,
  `book_newest_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `book_newest_url` int(10) UNSIGNED NULL DEFAULT NULL,
  `book_desc` varchar(350) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `image_paths` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `book_id_index`(`book_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1007 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Compact;

SET FOREIGN_KEY_CHECKS = 1;

import {
  Flex, HStack,
  Menu, MenuButton, MenuList, MenuItem, MenuDivider,
  Avatar,
  Heading, Text, Button,
} from "@chakra-ui/react"
import { ChevronDownIcon } from "@chakra-ui/icons"
import React from "react"

// TODO: 色設定・ログイン判定などの処理

const isLoggedIn = true

const Header: React.FC = () => {
  return (
    <Flex
      as="header"
      align="center"
      justify="space-between"
      wrap="wrap"
      paddingY={2}
      paddingX={4}
      bg="gray.700"
    >
      <Heading as="h1" size="sm" textColor="white">
        Sekigae Service
      </Heading>
      {
        isLoggedIn ? (
          <Menu>
            <MenuButton
              textColor="white"
            >
              <HStack alignItems="center" spacing="1">
                <Avatar
                  size="xs"
                  name="Dan Abrahmov"
                  src="https://bit.ly/dan-abramov"
                />
                <ChevronDownIcon />
              </HStack>
            </MenuButton>
            <MenuList>
              <Text fontSize="xs" textAlign="center">Dan としてログイン中</Text>
              <MenuDivider />
              <MenuItem>アカウント情報</MenuItem>
              <MenuItem>席替えをする</MenuItem>
              <MenuDivider />
              <MenuItem>ログアウト</MenuItem>
            </MenuList>
          </Menu>
        ) : (
          <Button size="xs" padding="2">ログインする</Button>
        )
      }
    </Flex>
  )
}

export default Header
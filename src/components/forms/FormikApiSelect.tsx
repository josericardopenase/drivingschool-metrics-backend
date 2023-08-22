import React, { useState } from 'react';
import {
  Menu,
  MenuButton,
  MenuList,
  Button,
  Input,
  Box,
  Icon,
  Flex,
} from '@chakra-ui/react';
import { useField } from 'formik';
import { IoCheckmark, IoChevronDown } from 'react-icons/io5';
// Make sure to import ApiService and listApiResponse correctly
// from their respective paths.
import { ApiService } from '../../engines/http-plank/src/core/client';
import { listApiResponse } from '../../engines/http-plank/src/types/apitypes';

interface Props<T extends { id?: number }> {
  label: React.ReactNode | string;
  name: string;
  single?: boolean;
  apiService: ApiService<T, any, listApiResponse<T>>;
  children: (x: T) => React.ReactNode;
}

function FormikApiSelect<T extends { id?: number }>(props: Props<T>) {
  const [text, setText] = useState('');

  const [field, meta, helpers] = useField(props.name);
  const { data, fetchNextPage } = props.apiService.useInfiniteList({ search: text });

  function toggleValue(id: any) {
    if (props.single) {
      if (field.value === id) {
        helpers.setValue(null);
      } else {
        helpers.setValue(id);
      }
    } else {
      if (field.value.includes(id)) {
        helpers.setValue(field.value.filter((x: any) => x !== id));
      } else {
        helpers.setValue([...field.value, id]);
      }
    }
  }

  return (
    <Menu closeOnSelect={false}>
      <MenuButton rightIcon={<Icon as={IoChevronDown} />} as={Button} colorScheme='gray'>
        {props.label}
      </MenuButton>
      <MenuList minWidth='240px' overflow='hidden'>
        <Box p='2'>
          <Input size='sm' placeholder='search...' onChange={(e) => setText(e.target.value)} />
        </Box>
        <Box defaultValue='asc' title='Order' overflow='auto' maxH='200px'>
          {data?.pages.map((x) =>
            x.results.map((y) => (
              <Flex
                key={y.id}
                cursor='pointer'
                alignItems='center'
                px='4'
                py='1'
                onClick={() => {
                  toggleValue(y?.id ?? 0);
                }}
              >
                {props.single ? (
                  field.value === y.id ? (
                    <Icon color='green.500' as={IoCheckmark} />
                  ) : null
                ) : field.value.includes(y.id) ? (
                  <Icon color='green.500' as={IoCheckmark} />
                ) : null}
                {props.children(y)}
              </Flex>
            ))
          )}
        </Box>
      </MenuList>
    </Menu>
  );
}

export default FormikApiSelect;

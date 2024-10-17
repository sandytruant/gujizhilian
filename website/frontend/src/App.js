// import * as React from 'react'
import React, { useState, useEffect, useRef } from 'react'
import {
  CssVarsProvider,
  useJoyTheme,
  Modal,
  Button,
  Stack,
  TextField,
  Grid,
  Checkbox,
  Snackbar,
  IconButton,
  Box,
  Card,
  Typography,
  Autocomplete,
  Input,
  Skeleton,
  List,
  ListItem,
  ListItemDecorator,
  Radio,
  RadioGroup,
  FormControl,
  FormLabel,
  FormHelperText,
  Sheet,
} from '@mui/joy'

// import '@fontsource/inter'; // 字体
import { styled } from '@mui/joy/styles'
import 'slick-carousel/slick/slick.css'
import 'slick-carousel/slick/slick-theme.css'

// import { useSpring, animated } from 'react-spring' // Spring 动画库

function Info () {
  return (
    <Stack
    sx={{
      py: 3,
      px: 2,
      mt: 'auto',
      color: 'text.secondary',
      textAlign: 'left'
    }} spacing={2}
  >
  
      <Typography level='title-md'>使用方法</Typography>
        <Typography level='body-md'>
          📚在输入框内按类似输入法的使用习惯输入。
          <br />
          ⌨️使用上、下方向键选择语句。
          <br />
          👌按 Tab 键复制该语句。
        </Typography>
        <Typography level='title-md'>更适合中文宝宝体质的输入法</Typography>
        <Typography level='body-md'>
          古籍智联（暂时取了个很土的名字，大家可以想想这个工具叫什么）是一款待开发的中文输入法插件，目标是能够根据输入的部分拼音直接联想出可能的对应古籍中的完整语句，以解决当下主流输入法输入古籍中语句效率低下的问题。
        </Typography>

        <Typography level='title-sm'>施工计划</Typography>
        <Typography level='body-sm'>
          1.
          古籍资源建设：①添加出处、版本信息；②应该以分句为单位补全，还是以整句为单位补全？
          2. 前端开发：响应式布局，美化，Tab键Bug修复，复制出处信息/版本信息 3.
          后端开发：繁简转换，模糊匹配
          （模糊匹配需求：①只输入声母，不输入韵母，得到结果；②输入为句子中不连续的若干音节；③输入为汉字和拼音混合（可转化为②）；④其他模糊匹配需求）
        </Typography>
        <Typography level='body3'>
      &copy; {new Date().getFullYear()} · 《中文工具书》课程作业
    </Typography>
        </Stack>
  )
}

function Settings () {
  const Item = styled(Sheet)(({ theme }) => ({
    ...theme.typography['body-sm'],
    // textAlign: 'center',
    fontWeight: theme.fontWeight.md,
    color: theme.vars.palette.text.secondary,
    border: '1px solid',
    borderColor: theme.palette.divider,
    padding: theme.spacing(2),
    borderRadius: theme.radius.md,
    flexGrow: 1
  }))
  return (
    <Box>
    <Typography level='title-md'>偏好设置</Typography>
    <Stack spacing={1} direction='row' useFlexGap sx={{ flexWrap: 'wrap' }}>
      <Item>
        <FormControl>
          <FormLabel>首选项</FormLabel>
          <RadioGroup defaultValue='medium' name='radio-buttons-group'>
            <Radio value='small' label='大陆简体' size='sm' />
            <Radio value='small' label='大陆繁体' size='sm' />
          </RadioGroup>
          <Box sx={{ display: 'flex', gap: 3, pt: 1 }}>
            <Checkbox label='开启模糊匹配' size='sm' defaultChecked />
          </Box>
        </FormControl>
      </Item>

      <Item>
        <FormControl>
          <FormLabel>复制</FormLabel>
          <RadioGroup
            defaultValue='medium'
            name='radio-buttons-group'
          ></RadioGroup>
          <Box sx={{ display: 'flex', gap: 3, pt: 0 }}>
            <Checkbox label='复制出处信息' size='sm' defaultChecked />
          </Box>
          <Box sx={{ display: 'flex', gap: 3, pt: 2 }}>
            <Checkbox label='复制版本信息' size='sm' defaultChecked />
          </Box>
        </FormControl>
      </Item>
      <Item>
        <FormControl>
          <FormLabel>Sizes</FormLabel>
          <RadioGroup defaultValue='medium' name='radio-buttons-group'>
            <Radio value='small' label='Small' size='sm' />
            <Radio value='medium' label='Medium' size='md' />
          </RadioGroup>
        </FormControl>
      </Item>
    </Stack>
    </Box>
  )
}




const SearchComponent = () => {
  const [query, setQuery] = useState('')
  const [results, setResults] = useState([])
  const [selectedIndex, setSelectedIndex] = useState(-1) // 新增状态，跟踪选中的结果索引
  const resultsRef = useRef([])
  const [snackbarOpen, setSnackbarOpen] = useState(false) // 新增状态，用于控制Snackbar的显示

  useEffect(() => {
    const handleKeyDown = event => {
      if (['ArrowDown', 'ArrowUp', 'Tab'].includes(event.key)) {
        event.preventDefault()
      }

      if (event.key === 'ArrowDown') {
        setSelectedIndex(prevIndex =>
          prevIndex < results.length - 1 ? prevIndex + 1 : 0
        )
      } else if (event.key === 'ArrowUp') {
        setSelectedIndex(prevIndex =>
          prevIndex > 0 ? prevIndex - 1 : results.length - 1
        )
      } else if (event.key === 'Tab' && selectedIndex >= 0) {
        copyResultToSearch(results[selectedIndex])
        copyResultToClipboard(results[selectedIndex])
      }
    }

    window.addEventListener('keydown', handleKeyDown)
    return () => window.removeEventListener('keydown', handleKeyDown)
  }, [selectedIndex, results])

  const handleSearch = async event => {
    setQuery(event.target.value)
    if (event.target.value.length > 1) {
      const searchResults = await searchFunction(event.target.value)
      setResults(searchResults)
      setSelectedIndex(-1) // 重置选中索引
    } else {
      setResults([])
      setSelectedIndex(-1) // 重置选中索引
    }
  }

  const searchFunction = async query => {
    try {
      const response = await fetch(
        `https://10.129.82.37:5001/search?query=${encodeURIComponent(query)}`
      )
      if (!response.ok) {
        throw new Error('Network response was not ok')
      }
      const results = await response.json()
      return results
    } catch (error) {
      console.error(
        'There has been a problem with your fetch operation:',
        error
      )
      return [] // 返回空数组以避免在前端抛出错误
    }
  }

  const copyResultToSearch = result => {
    setQuery(result.name)
    setResults([]) // 可选：搜索后将结果列表清空
  }

  const copyResultToClipboard = result => {
    navigator.clipboard
      .writeText(result.name)
      .then(() => {
        setSnackbarOpen(true) // 复制成功后，显示Snackbar
      })
      .catch(error => {
        console.error('Failed to copy text: ', error)
      })
  }

  const handleSnackbarClose = (event, reason) => {
    if (reason === 'clickaway') {
      return
    }
    setSnackbarOpen(false)
  }

  useEffect(() => {
    if (selectedIndex >= 0 && resultsRef.current[selectedIndex]) {
      resultsRef.current[selectedIndex].focus()
    }
  }, [selectedIndex])


  function InputArea () {
    return (
      1
    )
  } 

  
  return (
    <div style={{ textAlign: 'center', width: '100%' }}>
      <Stack style={{ textAlign: 'center', height: '100%' }} spacing={1.5}>
        <Card
          sx={{
            border: 0,
            borderRadius: 0,
            sha: '1 1 1 1 #000',
            height: '100vh',
            minHeight: "710px",
            backgroundImage:
              'url(https://gd-hbimg.huaban.com/b2c5685f44cc38c2e41848651c1943d249768affb7f68-ygJvee_fw1200webp)',
            backgroundAttachment: 'fixed',
            
          }}
        >
          <div style={{position: "absolute", bottom: "10vh", width: "98vw", textAlign: 'center'}}>
            向下滑动查看更多
          </div>


           {/* <div style={{ position: 'sticky', top: 0}}> */}
          <center>
            <img
              src='logo.png'
              style={{ width: '100px', paddingTop: '10vh',}}
            />
          </center>
          {/* </div> */}

          <center>
            <Stack style={{ maxWidth: 800, textAlign: 'left' }} spacing={1.5}>
              <Card
                size='md'
                sx={{
                  backdropFilter: 'blur(20px)',
                  backgroundColor: 'rgba(255,255,255,0.5)'
                }}
              >
                <Typography level='body-sm'>
                  在下方的输入框内试一试叭
                </Typography>
                <Input
                  label='Search'
                  value={query}
                  onChange={handleSearch}
                  fullWidth
                  sx={{ mb: 2 }}
                />
                <Box sx={{ maxHeight: '300px', overflowY: 'auto' }}>
                  {results.map((result, index) => (
                    <Box
                      key={result.id}
                      ref={el => (resultsRef.current[index] = el)}
                      tabIndex={0} // 添加tabIndex以使Box可聚焦
                      sx={{
                        p: 1,
                        borderBottom: '1px solid',
                        borderColor: 'neutral.outlinedBorder',
                        backgroundColor:
                          selectedIndex === index
                            ? 'action.hover'
                            : 'background.paper',
                        cursor: 'pointer'
                      }}
                      onFocus={() => setSelectedIndex(index)}
                      onBlur={() => setSelectedIndex(-1)}
                      onMouseEnter={() => setSelectedIndex(index)}
                      onMouseLeave={() => setSelectedIndex(-1)}
                      onClick={() => copyResultToSearch(result)}
                    >
                      <Typography level='body2'>{result.name}</Typography>
                      <Typography level='body3' sx={{ color: 'text.tertiary' }}>
                        {result.description}
                      </Typography>
                    </Box>
                  ))}
                </Box>
              </Card>
            </Stack>
          </center>
        

        {/* Snackbar提示 */}
        <Snackbar
          open={snackbarOpen}
          anchorOrigin={{ vertical: 'top', horizontal: 'center' }}
          autoHideDuration={1000}
          onClose={handleSnackbarClose}
          message='文本已复制到剪贴板'
          action={
            <IconButton
              size='small'
              aria-label='close'
              color='inherit'
              onClick={handleSnackbarClose}
            >
              {/* <CloseIcon fontSize="small" /> */}
            </IconButton>
          }
        >
          ❤️文本已复制到剪贴板
        </Snackbar>
        </Card>
      </Stack>
      <Stack
        style={{
          padding: 50,
          maxWidth: 800,
          display: 'inline-block',
          textAlign: 'left'
        }}
        spacing={1.5}
      >
        
        <Settings/>
        <Info/>

      </Stack>
    </div>
  )
}

export default SearchComponent
